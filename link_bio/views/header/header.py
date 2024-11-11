import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.colors import TextColor as TextColor
def header() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/photo.png",
            width="150px",
            height="auto",
            margin="0 auto",
            border_radius="15px 50px",
            border="5px solid transparent",
            background="linear-gradient(144deg, #F58529, #DD2A7B, #8134B8, #A32DB6)",
            background_clip="border-box",
            alt="Logo personal"
                
            #border="5px solid #555",
        ),
        rx.heading("Raúl Espinoza!", size="9", align="center",
                   color= TextColor.BODY.value),
        rx.text("Devops Engineer", size="6",
                color= TextColor.BODY.value),
        rx.text("""I am a technology enthusiast with hands-on experience in DevOps, infrastructure automation, Bash scripting, and languages like Golang and Python. I hold the Azure Fundamentals (AZ-900) certification and have worked on projects that strengthen my skills in DevOps, Jenkins, cloud automation, and Bash scripting. 
                I am seeking an opportunity in a dynamic team where I can continue developing as a DevOps Engineer and contribute innovative solutions that optimize automation and efficiency!!""",
                color= TextColor.BODY.value),
                padding="1em"
        ),
        