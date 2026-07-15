import argparse, json
from datetime import datetime

parser = argparse.ArgumentParser(description="A simple command-line tool.")

parser.add_argument("id", type=int)
parser.add_argument("task", type=str)
parser.add_argument("status", type=str)

args = parser.parse_args()


createdAT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

task_dict= {
  "id": args.id,
  "task": args.task,
  "status": args.status,
  "createdAt":createdAT,
  "updatedAt":updatedAt,
}


print(task_dict)

