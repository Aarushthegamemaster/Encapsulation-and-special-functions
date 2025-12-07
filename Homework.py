class StringReverser:

    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        self.text = text

    def reverse(self) -> str:
        return self.text[::-1]

    def __str__(self):
        return f"Original: {self.text} | Reversed: {self.reverse()}"


if __name__ == "__main__":
    try:
        user_input = input("Enter a string to reverse: ").strip()

        if not user_input:
            print("Error: Empty string provided.")
        else:
            reverser = StringReverser(user_input)
            print(f"Reversed string: {reverser.reverse()}")

    except Exception as e:
        print(f"An error occurred: {e}")

