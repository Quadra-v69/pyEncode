import os
import base64
import sys
import time

# Colors using ANSI escape codes (works without colorama)
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RED = "\033[91m"
RESET = "\033[0m"

def slow_print(text, delay=0.002):
    """Print text character by character for animation effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_banner():
    banner = f"""
{CYAN}██████╗ ██╗   ██╗███████╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗
██╔══██╗╚██╗ ██╔╝██╔════╝████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝
██████╔╝ ╚████╔╝ █████╗  ██╔██╗ ██║██║     ██║   ██║██║  ██║█████╗  
██╔═══╝   ╚██╔╝  ██╔══╝  ██║╚██╗██║██║     ██║   ██║██║  ██║██╔══╝  
██║        ██║   ███████╗██║ ╚████║╚██████╗╚██████╔╝██████╔╝███████╗
╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                    
{MAGENTA}                            🔹 PYENCODE 🔹{RESET}
{YELLOW}    ------------------------------------------------------------------
          {GREEN}Developed by:{WHITE} Quadra_v69
          {GREEN}Instagram:  {WHITE}instagram.com/reflame.x
          {GREEN}GitHub:     {WHITE}github.com/quadra-v69
          {GREEN}X (Twitter):{WHITE}x.com/quadra_v69
          {GREEN}LinkedIn:   {WHITE}linkedin.com/in/rantu-dev
{YELLOW}    ------------------------------------------------------------------{RESET}
"""
    slow_print(banner, 0.0008)  # Smooth hacker-style animation

def obfuscate_file(input_file, output_file):
    """Obfuscate a single Python file into Base64 one-liner"""
    with open(input_file, "r", encoding="utf-8") as f:
        code = f.read()

    encoded = base64.b64encode(code.encode("utf-8")).decode("utf-8")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"import base64;exec(compile(base64.b64decode('{encoded}'),'<string>','exec'))")

    print(f"{GREEN}✅ Obfuscated:{CYAN} {input_file} {WHITE}→ {YELLOW}{output_file}{RESET}")

def obfuscate_project(input_path, output_path):
    """Obfuscate a single file or an entire folder"""
    if os.path.isfile(input_path):
        # Only create a directory if there is one in the path
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        obfuscate_file(input_path, output_path)
    else:
        for root, _, files in os.walk(input_path):
            for file in files:
                if file.endswith(".py"):
                    full_input = os.path.join(root, file)
                    relative_path = os.path.relpath(full_input, input_path)
                    full_output = os.path.join(output_path, relative_path)

                    os.makedirs(os.path.dirname(full_output), exist_ok=True)
                    obfuscate_file(full_input, full_output)
if __name__ == "__main__":
    print_banner()
    slow_print(f"{CYAN}=== Python Base64 Obfuscator ==={RESET}", 0.005)

    input_path = input(f"{YELLOW}🔹 Enter your Python file or folder path: {RESET}").strip()
    if not os.path.exists(input_path):
        print(f"{RED}❌ Error: File or folder not found!{RESET}")
        exit()

    output_path = input(f"{YELLOW}🔹 Enter output folder or file path: {RESET}").strip()

    obfuscate_project(input_path, output_path)
    slow_print(f"\n{GREEN}🎉 All files obfuscated successfully!{RESET}", 0.004)
