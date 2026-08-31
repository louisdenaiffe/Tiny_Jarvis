import sys
import time
from main import initialize, handle_prompt


def run_cli_test():
    d = initialize(listen=False)

    print("\n==========================================")
    print("      TINY JARVIS - CLI TEST MODE        ")
    print("==========================================")
    print("Type your prompt and press Enter.")
    print("Type 'exit' or 'quit' to stop.\n")

    try:
        while True:
            prompt = input("You > ").strip()

            if not prompt:
                continue
            if prompt.lower() in ["exit", "quit"]:
                print("Exiting CLI Mode...")
                break

            start_time = time.perf_counter()
            first_token_time = None

            response = handle_prompt(prompt, d)
            print("Tiny_Jarvis > ", end="", flush=True)

            if isinstance(response, str):
                first_token_time = time.perf_counter()
                print(response)
            elif response:
                for chunk in response:
                    if first_token_time is None:
                        first_token_time = time.perf_counter()
                    print(chunk, end="", flush=True)
                print()

            end_time = time.perf_counter()
            if first_token_time:
                ttft_ms = (first_token_time - start_time) * 1000
                total_sec = end_time - start_time
                print(f"\n--- [ Performance Metrics ] ---")
                print(f"• TTFT (Time to First Token): {ttft_ms:.1f} ms")
                print(f"• Total Generation Time:     {total_sec:.2f} s")
                print("--------------------------------\n")
            else:
                print()
    except KeyboardInterrupt:
        print("\nExiting CLI testing mode...")
    finally:
        d.stop()


if __name__ == "__main__":
    run_cli_test()
            




