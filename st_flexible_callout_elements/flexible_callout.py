import streamlit as st

def flexible_callout(
    message, 
    container=st, 
    background_color="#D9D9D9", 
    font_color="#000000", 
    font_size=16, 
    alignment="left",
    line_height=1.5,
    border_radius=8,
    padding=15,
    margin_bottom=20,
    icon=None,
    icon_size=None,
):
    """
    Display a flexible callout message box in Streamlit with customizable HTML and CSS.

    Arguments:
    - message (str): The message to display.
    - container: The Streamlit container to render the message in (default is st).
    - background_color (str): The background color of the message box.
    - font_color (str): The font color of the message text.
    - font_size (int): The font size of the message text in pixels.
    - alignment (str): The text alignment inside the message box ("left", "center", "right", "justify").
    - line_height (float): The line height of the message text.
    - border_radius (int): The border radius of the message box.
    - padding (int): The padding inside the message box in pixels.
    - margin_bottom (int): The margin below the message box in pixels.
    - icon (str): Appears on the left side of the box. Supports emojis (e.g., "ℹ️", "🚨") or Material Icons (e.g., ":material/info:").
    - icon_size (int): Icon size in pixels. If not defined, uses font_size.
    """

    if not icon:
        container.markdown(f"""
            <div style="
                background-color: {background_color};
                color: {font_color};
                font-size: {font_size}px;
                text-align: {alignment}; 
                line-height: {line_height};
                border-radius: {border_radius}px;
                padding: {padding}px;
                margin-bottom: {margin_bottom}px;
            ">
                {message}
            </div>
        """, unsafe_allow_html=True)

    else:
        if icon_size is None:
            icon_size = font_size
        
        font_link = ""
        icon_content = ""
        
        # Handle Material Design icons
        if icon.startswith(":material/") and icon.endswith(":"):
            icon_name = icon[10:-1]
            font_link = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />'
            icon_content = f'<span class="material-symbols-rounded" style="font-size: {icon_size}px; color: {font_color};">{icon_name}</span>'
        else:
            # Handle emoji or other text icons
            icon_content = f'<span style="font-size: {icon_size}px;">{icon}</span>'
        
        container.markdown(f"""
            {font_link}
            <div style="
                background-color: {background_color};
                border-radius: {border_radius}px;
                padding: {padding}px;
                margin-bottom: {margin_bottom}px;
                display: flex;
                align-items: center;
                gap: 8px;
            ">
                <div style="flex-shrink: 0;">
                    {icon_content}
                </div>
                <div style="
                    flex: 1;
                    color: {font_color};
                    font-size: {font_size}px;
                    text-align: {alignment}; 
                    line-height: {line_height};
                ">
                    {message}
                </div>
            </div>
        """, unsafe_allow_html=True)

def flexible_error(message, container=st, font_size=16, alignment="left", line_height=1.5, border_radius=8, padding=15, margin_bottom=20, icon=None, icon_size=None):
    """
    Display an error message with predefined styles.
    """
    flexible_callout(
        message, 
        container=container, 
        background_color="#ffecec", 
        font_color="#7d353b",
        font_size=font_size, 
        alignment=alignment,
        line_height=line_height,
        border_radius=border_radius,
        padding=padding,
        margin_bottom=margin_bottom,
        icon=icon, 
        icon_size=icon_size
    )

def flexible_success(message, container=st, font_size=16, alignment="left", line_height=1.5, border_radius=8, padding=15, margin_bottom=20, icon=None, icon_size=None):
    """
    Display a success message with predefined styles.
    """
    flexible_callout(
        message, 
        container=container, 
        background_color="#e8f9ee", 
        font_color="#177233",
        font_size=font_size, 
        alignment=alignment,
        line_height=line_height,
        border_radius=border_radius,
        padding=padding,
        margin_bottom=margin_bottom,
        icon=icon, 
        icon_size=icon_size
    )

def flexible_warning(message, container=st, font_size=16, alignment="left", line_height=1.5, border_radius=8, padding=15, margin_bottom=20, icon=None, icon_size=None):
    """
    Display a warning message with predefined styles.
    """
    flexible_callout(
        message, 
        container=container, 
        background_color="#fffce7", 
        font_color="#95700b",
        font_size=font_size,
        alignment=alignment, 
        line_height=line_height,
        border_radius=border_radius,
        padding=padding,
        margin_bottom=margin_bottom,
        icon=icon, 
        icon_size=icon_size
    )

def flexible_info(message, container=st, font_size=16, alignment="left", line_height=1.5, border_radius=8, padding=15, margin_bottom=20, icon=None, icon_size=None):
    """
    Display an info message with predefined styles.
    """
    flexible_callout(
        message, 
        container=container, 
        background_color="#e8f2fc", 
        font_color="#0d4c87",
        font_size=font_size, 
        alignment=alignment,
        line_height=line_height,
        border_radius=border_radius,
        padding=padding,
        margin_bottom=margin_bottom,
        icon=icon, 
        icon_size=icon_size
    )
