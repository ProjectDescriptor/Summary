import streamlit as st
import os
import io




st.title("Video Description")

uploaded_file = st.file_uploader("Video File", type=['mp4', 'webm', 'mov', 'avi'])
temporary_location = False

if uploaded_file is not None:
    g = io.BytesIO(uploaded_file.read())  ## BytesIO Object
    temporary_location = "C:/Users/HP/Desktop/Project/Video_Output/testout_simple.mp4"

    with open(temporary_location, 'wb') as out:  ## Open temporary file as bytes
        out.write(g.read())  ## Read bytes into file

    # close file
    out.close()
     
    Doc_btn = st.button('Get Description')
    if Doc_btn:
      st.write("Happy now")
      # starter()

@st.cache(allow_output_mutation=True)
def get_cap(location):
    print("Loading in function", str(location))
    video_stream = cv2.VideoCapture(str(location))

    # Check if camera opened successfully
    if (video_stream.isOpened() == False):
        print("Error opening video  file")
    return video_stream


scaling_factorx = 0.25
scaling_factory = 0.25
image_placeholder = st.empty()

if temporary_location:
    while True:
        # here it is a CV2 object
        video_stream = get_cap(temporary_location)
        # video_stream = video_stream.read()
        ret, image = video_stream.read()
        if ret:
            image = cv2.resize(image, None, fx=scaling_factorx, fy=scaling_factory, interpolation=cv2.INTER_AREA)
        else:
            print("there was a problem or video was finished")
            cv2.destroyAllWindows()
            video_stream.release()
            break
        # check if frame is None
        if image is None:
            print("there was a problem None")
            # if True break the infinite loop
            break

        image_placeholder.image(image, channels="BGR", use_column_width=True)

        cv2.destroyAllWindows()
    video_stream.release()


    cv2.destroyAllWindows()
