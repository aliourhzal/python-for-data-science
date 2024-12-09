from os import get_terminal_size

def ft_tqdm(lst: range) -> None:
    for i in lst:
        step = i + 1
        terminal_width = get_terminal_size().columns - 25
        progress = round(step * 100 / len(lst))
        bar_width = terminal_width - (len(str(progress)) + 2) - (2 + len(str(step)) + 1 + len(str(len(lst))))
        bar_count = round(bar_width * progress / 100)
        bar = "█" * bar_count
        spaces = " " * (bar_width - bar_count)
        print(f"{progress}%|{bar}{spaces}| {step}/{len(lst)}", end="\r")
        yield None
