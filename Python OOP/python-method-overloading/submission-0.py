class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, text1 : str, text2 : str = None):
        if text2:
            text3 = text1 + text2
            return text3
        else:
            return text1.upper()
            







# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
