import pywebio
from pywebio.output import put_html, put_text, put_buttons, clear
from pywebio.session import run_js
import base64

# --- Configuration ---
# You need to provide the paths to your video files here.
BACKGROUND_VIDEO_PATH = "img/glitch background - Yury Zaytsev (1080p, h264).mp4"
MAIN_VIDEO_PATH = "img/111.mp4"

def play_video():
    """This function is called when the 'Play' button is clicked."""
    clear()  # Clear the screen (removes the button and text)
    
    # Read the main video file and encode it to base64
    # This is needed to embed the video directly in the HTML
    with open(MAIN_VIDEO_PATH, "rb") as video_file:
        video_base64 = base64.b64encode(video_file.read()).decode('utf-8')

    # Display the main video, set to autoplay with sound
    put_html(f"""
        <div class="video-placeholder">
            <video id="main-pywebio-video" autoplay controls style="width: 100%; height: 100%; border-radius: 12px;">
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
    """)
    # Use run_js to set the video volume to maximum after it's added to the page
    run_js("""
        document.getElementById('main-pywebio-video').volume = 1.0;
    """)
    put_text("IF YOU WATCH THE VIDEO, YOUR CELLPHONE WILL GO CRAZY").style('color: #f80000; text-align: center; margin-top: 32px;')

def main():
    """The main application function."""
    # Set the background video using custom CSS and JavaScript
    run_js(f'document.body.style.backgroundImage = "url({BACKGROUND_VIDEO_PATH})";') # Note: This is a simplified approach. For a true video bg, more complex JS is needed via PyWebIO.
    
    put_text("KINDLY PLAY THE VIDEO").style('color: #f80000; font-size: 2.5em; font-weight: bold; text-align: center; margin-bottom: 32px;')
    put_buttons(['PLAY'], onclick=[play_video])

if __name__ == '__main__':
    pywebio.start_server(main, port=8080, debug=True)