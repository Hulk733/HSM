def register():
    print("Voice-to-code plugin active")

def transcribe_and_parse(voice_input):
    return f"""def hello():
    print('{voice_input}')"""
