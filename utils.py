import replicate


def answer_image_question(image_name, question):
    output = replicate.run(
        "andreasjansson/blip-2:4b32258c42e9efd4288bb9910bc532a69727f9acd26aa08e175713a0a857a608",
        input={"image": open(image_name, "rb"), "question": question},
    )
    return output


def generate_greeting(style, description_of_costumes):
    system_prompt = f"""
        You are going to scare trick or treaters in the style of {style}.

        This is for Halloween, so you should be as creepy and scary as you possibly can.

        Try to keep things short.

        The user is going to explain who is there costume wise and you should use your scary style of {style} but address the trick or treaters to scare them personally.
    """
    output = replicate.run(
        "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        input={
            "prompt": description_of_costumes,
            "system_prompt": system_prompt,
        },
    )

    return "".join(output) 


def generate_video(image_file_name, audio_file_name):
    print("image_file_name", image_file_name)
    print("audio_fie_nae", audio_file_name)
    output = replicate.run(
        "cjwbw/sadtalker:3aa3dac9353cc4d6bd62a8f95957bd844003b401ca4e4a9b33baa574c549d376",
        input={
            "source_image": open(image_file_name, "rb"),
            "driven_audio": open(audio_file_name, "rb"),
        }
    )
    return output