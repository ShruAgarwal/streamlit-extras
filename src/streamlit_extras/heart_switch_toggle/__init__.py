import streamlit as st
from streamlit_custom_toggle import st_custom_toggle

from .. import extra

st_custom_toggle = extra(st_custom_toggle)


def example():
    st.write("## Heart-shaped Toggle Switch")
    st_custom_toggle(
        label="Disabled",
        active_track_fill="#EAE4E4",
        active_thumb_color="#EAE4E4",
        value="true",  # optional
        key="toggle1",
    )

    fruit_toggle = st_custom_toggle(
        label="Active",
        active_track_fill="#57FD6E",
        active_thumb_color="#052754",
        key="toggle2",
    )

    fruit = st.radio(
        "Select your favorite fruit",
        ("Mango", "Watermelon", "Grapes", "Apple", "Orange"),
        disabled=fruit_toggle,
    )
    st.markdown(f"You love: {fruit}")


def _play_with_toggle():
    toggle_value = st.selectbox("Choose style", ("false", "true"))

    with st.expander("Customize colors 🎨"):
        st.info("This is effective only when the toggle is active!")

        track_color = st.selectbox(
            "Track Fill Color", options=("default", "custom_track")
        )
        if track_color == "default":
            track_color = "#F51EF8"

        # Set track color
        if track_color == "custom_track":
            track_color = st.color_picker("Pick a color", key=track_color)

        thumb_color = st.selectbox("Thumb Color", options=("default", "custom_thumb"))
        if thumb_color == "default":
            thumb_color = "#900C3F"

        # Set thumb color
        if thumb_color == "custom_thumb":
            thumb_color = st.color_picker("Pick a color", key=thumb_color)

    st_custom_toggle(
        label="Test Toggle",
        active_track_fill=track_color,
        active_thumb_color=thumb_color,
        value=toggle_value,
        key="toggle_test",
    )


__title__ = "Heart Toggle Switch"
__desc__ = "On/Off Heart-shaped Toggle Switch widget with color customizations"
__icon__ = "💜"
__examples__ = [example]
__author__ = "ShruAgarwal"
__pypi_name__ = "streamlit-custom-toggle"
__package_name__ = "streamlit_custom_toggle"
__github_repo__ = "https://github.com/ShruAgarwal/streamlit-custom-toggle"
__forum_url__ = "https://discuss.streamlit.io/t/streamlit-custom-toggle-a-custom-component-to-load-heart-shaped-toggle-switch-widget/32499"
__experimental_playground__ = True
__experimental_playground_funcs__ = [_play_with_toggle]
