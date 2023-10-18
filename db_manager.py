import sqlite3


class Database:

    def __init__(self, db_path: str) -> None:
        self.db = sqlite3.connect(db_path, check_same_thread=False)
        self.sql = self.db.cursor()

    def create_task(self, title: str, description: str) -> None:
        if len(description):
            self.sql.execute(
                f"INSERT INTO tasks (task_title, task_description) VALUES ('{title}', '{description}')")
        else:
            self.sql.execute(
                f"INSERT INTO tasks (task_title) VALUES ('{title}')")

        self.db.commit()
        print(f"[i] Task \"{title}\" Created successfully!")

    def get_tasks(self) -> list:
        self.sql.execute("SELECT * FROM tasks")
        tasks = self.sql.fetchall()
        print("[i] Tasks loaded.")

        return tasks

    def delete_task(self, _id: int) -> None:
        self.sql.execute(f"DELETE FROM tasks WHERE id={_id}")
        self.db.commit()
        print(f"[i] Task number {_id} deleted successfully.")

    def create_shoping(self, title: str) -> None:
        self.sql.execute(f"INSERT INTO shoping (title) VALUES ('{title}')")
        self.db.commit()
        print(f"[i] Shoping \"{title}\" Created successfully!")

    def get_shoping(self) -> list:
        self.sql.execute("SELECT * FROM shoping")
        shoping = self.sql.fetchall()
        print("[i] Shoping loaded.")

        return shoping

    def delete_shoping(self, _id: int) -> None:
        self.sql.execute(f"DELETE FROM shoping WHERE id={_id}")
        self.db.commit()
        print(f"[i] Shoping number {_id} deleted successfully.")


if __name__ == "__main__":
    print("[!] This file is to import only.")
