"""Home page shown when the user enters the application"""
import streamlit as st

import awesome_streamlit as ast

from PIL import Image
# pylint: disable=line-too-long

# image = Image.open("./src/img/img.jpg")
# st.image(image, use_column_width=True)
def write():
    """Used to write the page in the app.py file"""
    image = Image.open("./src/img/1.png")
    st.sidebar.image(image, use_column_width=True)
    st.markdown('<h2><b><font color=‘#5bc0de’> <i><u>BI Project : </u></i> DSEN-1-A 2021/2022 !</font></b></h2>', unsafe_allow_html=True)
    with st.spinner("Loading About ..."):
        # ast.shared.components.title_awesome(" - About")
        st.markdown('''
                <h3 style="font-family: cursive; color: rgb(255, 127, 39)"><b>SOme Images of our previous tests</b></h3>
                
                </p><hr style="border:1px solid black">
            ''', 
            unsafe_allow_html=True
        )

        st.markdown('''<p> Serie plot</p>''', unsafe_allow_html=True)
        #image = Image.open("./src/serieplot.PNG")
        #st.image(image, use_column_width=True)
        image = Image.open("./src/img/winter_plot.PNG")
        st.image(image, use_column_width=True)
        st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)

        st.markdown('''<p> winter model plot </p>''', unsafe_allow_html=True)
        image = Image.open("./src/img/winterplot.PNG")
        st.image(image, use_column_width=True)
        st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)

        st.markdown('''<p> winter model details</p> </div>''', unsafe_allow_html=True)
        image = Image.open("./src/img/winter_details.PNG")
        st.image(image, use_column_width=True)
        st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)

        st.markdown('''<p> winter forecastion untill 2025 </p> </div>''', unsafe_allow_html=True)
        image = Image.open("./src/img/winter_prediction.PNG")
        st.image(image, use_column_width=True)
        #st.image(Image.open("./src/img/export.png"), use_column_width=True)
        #st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)


        st.markdown('''<h2> SIMPLE ETS </h2> </div>''', unsafe_allow_html=True)
        st.markdown('''<p> Simple plot </p> </div>''', unsafe_allow_html=True)
        image = Image.open("./src/img/simple_plot.PNG")
        st.image(image, use_column_width=True)
        st.markdown('''<p> SIMPLE ETS Details </p> </div>''', unsafe_allow_html=True)
        image = Image.open("./src/img/simple_details.PNG")
        st.image(image, use_column_width=True)
        st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)
        
        st.markdown('''<p> SIMPLE ETS Forecasting </p> </div>''', unsafe_allow_html=True)
        image = Image.open("./src/img/simple_forcast.PNG")
        st.image(image, use_column_width=True)
        st.markdown('''</p><hr style="border:1px solid black">''', unsafe_allow_html=True)


#         st.markdown(
#             """## Contributions
# This an open source project and you are very welcome to **contribute** your awesome
# comments, questions, resources and apps as
# [issues](https://github.com/MarcSkovMadsen/awesome-streamlit/issues) or
# [pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls)
# to the [source code](https://github.com/MarcSkovMadsen/awesome-streamlit).
# For more details see the [Contribute](https://github.com/marcskovmadsen/awesome-streamlit#contribute) section of the README file.
# ## The Developer
# This project is developed by Marc Skov Madsen. You can learn more about me at
# [datamodelsanalytics.com](https://datamodelsanalytics.com).
# Feel free to reach out if you wan't to join the project as a developer. You can find my contact details at [datamodelsanalytics.com](https://datamodelsanalytics.com).
# [<img src="https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/assets/images/datamodelsanalytics.png?raw=true" style="max-width: 700px">](https://datamodelsanalytics.com)
# """,
#             unsafe_allow_html=True,
#         )