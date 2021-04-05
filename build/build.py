import os

configs = [
    {
        "src" : "../shedule-main",
        "cmd" : "../build",
        "app" : "chedule-main.exe"
    },
    {
        "src" : "../shedule-changes",
        "cmd" : "../build",
        "app" : "chedule-changes.exe"
    },
    {
        "src" : "../bot",
        "cmd" : "../build",
        "app" : "bot.exe"
    }
]


def build(cfg: dict ) -> None:
    os.chdir(cfg["src"])
    os.system(f"go build .")
    os.system(f"move {cfg['app']} {cfg['cmd']}")


if __name__ == "__main__":
    [build(i) for i in configs]
