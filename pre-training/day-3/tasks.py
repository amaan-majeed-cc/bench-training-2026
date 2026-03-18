#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

STATUSES = {"todo", "done"}

@dataclass
class Task:
  id: int
  title: str
  status: str  # "todo" | "done"
  created_at: dt.datetime

  def to_dict(self) -> Dict[str, Any]:
    return {
      "id": self.id,
      "title": self.title,
      "status": self.status,
      "created_at": self.created_at.isoformat(),
    }

  @classmethod
  def from_dict(cls, raw: Dict[str, Any]) -> "Task":
    created_at_raw = raw.get("created_at")
    if not isinstance(created_at_raw, str):
      raise ValueError("Task.created_at is missing or not a string")
    try:
      created_at = dt.datetime.fromisoformat(created_at_raw)
    except ValueError as e:
      raise ValueError("Task.created_at is not a valid ISO datetime") from e

    status = raw.get("status")
    if status not in STATUSES:
      raise ValueError("Task.status must be 'todo' or 'done'")

    return cls(
      id=int(raw["id"]),
      title=str(raw["title"]),
      status=str(status),
      created_at=created_at,
    )

class TaskManager:
  """
  Task persistence lives in `tasks.json` next to this script.
  """

  def __init__(self, storage_path: Path):
    self.storage_path = storage_path
    self.tasks: List[Task] = []
    self.next_id: int = 1
    self._load()

  def _load(self) -> None:
    try:
      text = self.storage_path.read_text(encoding="utf-8")
    except FileNotFoundError:
      return

    try:
      raw = json.loads(text)
    except json.JSONDecodeError as e:
      raise ValueError(f"Storage file is corrupt JSON: {self.storage_path}") from e

    if isinstance(raw, dict):
      tasks_raw = raw.get("tasks", [])
      next_id = raw.get("next_id")
      if isinstance(next_id, int) and next_id >= 1:
        self.next_id = next_id
    elif isinstance(raw, list):
      tasks_raw = raw
    else:
      raise ValueError("Storage JSON must be an object or a list")

    if not isinstance(tasks_raw, list):
      raise ValueError("Storage JSON 'tasks' must be a list")

    tasks: List[Task] = []
    for i, t_raw in enumerate(tasks_raw):
      if not isinstance(t_raw, dict):
        raise ValueError(f"Task #{i} is not an object")
      tasks.append(Task.from_dict(t_raw))

    self.tasks = tasks
    if self.tasks:
      max_id = max(t.id for t in self.tasks)
      if self.next_id <= max_id:
        self.next_id = max_id + 1

  def _save(self) -> None:
    payload = {
      "tasks": [t.to_dict() for t in self.tasks],
      "next_id": self.next_id,
    }
    self.storage_path.write_text(
      json.dumps(payload, indent=2, sort_keys=True) + "\n",
      encoding="utf-8",
    )

  def add_task(self, title: str) -> Task:
    title = title.strip()
    if not title:
      raise ValueError("title must be non-empty")

    task = Task(
      id=self.next_id,
      title=title,
      status="todo",
      created_at=dt.datetime.now(),
    )
    self.tasks.append(task)
    self.next_id += 1
    self._save()
    return task

  def complete_task(self, task_id: int) -> Task:
    task = self._get_task(task_id)
    task.status = "done"
    self._save()
    return task

  def list_tasks(self, filter: Optional[str] = None) -> List[Task]:
    if filter is None:
      return list(self.tasks)

    filter = filter.strip().lower()
    if filter not in STATUSES:
      raise ValueError("filter must be either 'todo' or 'done'")

    return [t for t in self.tasks if t.status == filter]

  def delete_task(self, task_id: int) -> None:
    idx = None
    for i, t in enumerate(self.tasks):
      if t.id == task_id:
        idx = i
        break
    if idx is None:
      raise KeyError(task_id)

    del self.tasks[idx]
    self._save()

  def _get_task(self, task_id: int) -> Task:
    for t in self.tasks:
      if t.id == task_id:
        return t
    raise KeyError(task_id)

def _print_tasks(tasks: List[Task]) -> None:
  if not tasks:
    print("No tasks found.")
    return

  for t in tasks:
    created = t.created_at.isoformat(sep=' ', timespec='seconds')
    print(f"#{t.id} {t.title} [{t.status}] created {created}")

def main(argv: Optional[List[str]] = None) -> int:
  parser = argparse.ArgumentParser(description="Command-line task tracker")
  subparsers = parser.add_subparsers(dest="command", required=True)

  p_add = subparsers.add_parser("add", help="Add a new task")
  p_add.add_argument("title", help="Task title")

  p_done = subparsers.add_parser("done", help="Mark task as done")
  p_done.add_argument("id", type=int, help="Task id")

  p_list = subparsers.add_parser("list", help="List tasks")
  p_list.add_argument("--filter", choices=sorted(STATUSES), default=None, help="Filter by status")

  p_delete = subparsers.add_parser("delete", help="Delete a task")
  p_delete.add_argument("id", type=int, help="Task id")

  args = parser.parse_args(argv)

  storage_path = Path(__file__).resolve().parent / "tasks.json"
  try:
    manager = TaskManager(storage_path=storage_path)
    if args.command == "add":
      task = manager.add_task(args.title)
      print(f"Added task #{task.id}: {task.title}")
      return 0

    if args.command == "done":
      task = manager.complete_task(args.id)
      print(f"Marked task #{task.id} as done.")
      return 0

    if args.command == "list":
      _print_tasks(manager.list_tasks(args.filter))
      return 0

    if args.command == "delete":
      manager.delete_task(args.id)
      print(f"Deleted task #{args.id}.")
      return 0

    raise RuntimeError("Unhandled command")
  except KeyError as e:
    task_id = e.args[0]
    print(f"No task with id {task_id}.", file=sys.stderr)
    return 1
  except ValueError as e:
    print(f"Could not complete that: {e}", file=sys.stderr)
    return 1


if __name__ == "__main__":
  raise SystemExit(main())

