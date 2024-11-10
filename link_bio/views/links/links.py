import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.colors import TextColor as TextColor

def links() -> rx.Component:
    return rx.vstack(
        title("Proyectos y Redes"),
        link_button(
            "LinkedIn", 
            "Check out my profile!", 
            "https://www.linkedin.com/in/raul-espinoza-a320032b2/"
            ),
        link_button(
            "Script Bash", 
            "Bash script designed to automate the deployment process of applications in server environments.",
            "https://github.com/raulblend/deploy-script"
            ),   
        link_button(
            "Python_Reflex",
            "Web page fully developed in Python, using the Reflex framework to create an efficient and dynamic interface!", 
            "https://github.com/raulblend/web_app"
            ),  
        link_button(
            "GitHub!",
            "Explore my repositories to see examples of automated scripts, deployments, and more. Feel free to contact me!", 
            "https://github.com/raulblend"
            ),
        width="100%",
        padding="1em"

    )