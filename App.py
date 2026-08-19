import streamlit as st

st.set_page_config(
    page_title="Happy Birthday Mr. Devbrato Midha",
    page_icon="🎂",
    layout="centered"
)

# =========================
# PREMIUM CSS
# =========================
st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 20% 10%, #243b55 0%, transparent 35%),
        radial-gradient(circle at 80% 90%, #b8860b 0%, transparent 25%),
        linear-gradient(135deg, #07111f, #101c2e 50%, #080d16);
    color: white;
}

/* Main container */
.block-container {
    max-width: 850px;
    padding-top: 45px;
    padding-bottom: 40px;
}

/* Stars */
.stars {
    text-align: center;
    font-size: 22px;
    letter-spacing: 12px;
    margin-bottom: 20px;
    animation: sparkle 2s infinite alternate;
}

@keyframes sparkle {
    from {
        opacity: 0.5;
        transform: scale(0.98);
    }
    to {
        opacity: 1;
        transform: scale(1.03);
    }
}

/* Title */
.title {
    text-align: center;
    font-size: 54px;
    font-weight: 800;
    letter-spacing: 2px;
    background: linear-gradient(90deg, #f5d76e, #fff4b0, #d4af37);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #d7dde8;
    font-size: 20px;
    letter-spacing: 1px;
    margin-bottom: 30px;
}

/* Name */
.name {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    color: #f5d76e;
    margin: 15px 0 25px 0;
}

/* Cake */
.cake {
    text-align: center;
    font-size: 95px;
    margin: 10px 0 25px 0;
    animation: float 2s ease-in-out infinite;
}

@keyframes float {
    0%,100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-12px);
    }
}

/* Card */
.card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(245,215,110,0.35);
    border-radius: 25px;
    padding: 40px;
    box-shadow: 0 15px 45px rgba(0,0,0,0.35);
    backdrop-filter: blur(10px);
    margin-top: 20px;
}

/* Message */
.message {
    text-align: center;
    font-size: 20px;
    line-height: 1.9;
    color: #edf1f7;
}

.highlight {
    color: #f5d76e;
    font-weight: bold;
}

/* Divider */
.divider {
    width: 100px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #d4af37, transparent);
    margin: 25px auto;
}

/* Footer */
.footer {
    text-align: center;
    color: #9da8b8;
    font-size: 15px;
    margin-top: 35px;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #b8860b, #d4af37, #f5d76e);
    color: #111827;
    border: none;
    border-radius: 30px;
    font-size: 18px;
    font-weight: 700;
    padding: 14px 25px;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 25px rgba(245,215,110,0.4);
}
/* Mobile Responsive Design */

@media (max-width: 600px) {

    .block-container {
        padding: 25px 15px 30px 15px;
    }

    .title {
        font-size: 36px;
        letter-spacing: 1px;
    }

    .subtitle {
        font-size: 16px;
    }

    .name {
        font-size: 28px;
    }

    .cake {
        font-size: 70px;
    }

    .card {
        padding: 25px 18px;
        border-radius: 20px;
    }

    .message {
        font-size: 17px;
        line-height: 1.7;
    }

    .stars {
        font-size: 16px;
        letter-spacing: 6px;
    }

    .stButton > button {
        font-size: 16px;
        padding: 12px 18px;
    }

    .footer {
        font-size: 13px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================
# TOP
# =========================

st.markdown(
    '<div class="stars">✦ ✧ ✦ ✧ ✦</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">HAPPY BIRTHDAY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">A Special Birthday Tribute</div>',
    unsafe_allow_html=True
)


# =========================
# NAME
# =========================

st.markdown(
    '<div class="name">Mr. Devbrato Midha</div>',
    unsafe_allow_html=True
)


# =========================
# CAKE
# =========================

st.markdown(
    '<div class="cake">🎂</div>',
    unsafe_allow_html=True
)


# =========================
# MESSAGE CARD
# =========================

st.markdown("""
<div class="card">

<div class="message">

Wishing you a very

<br>

<span class="highlight">
Happy Birthday, Mr. Devbrato Midha! 🎉
</span>

<div class="divider"></div>

May this special day mark the beginning of
another wonderful year filled with

<br>

<strong>success, happiness, good health,
and new achievements.</strong>

<br><br>

Your leadership, guidance and experience
continue to inspire those around you.

<br><br>

May the year ahead bring you
many more milestones to celebrate
and countless memorable moments.

<br><br>

<span class="highlight">
Wishing you a fantastic birthday
and a truly successful year ahead! 🌟
</span>

</div>

</div>
""", unsafe_allow_html=True)


# =========================
# SURPRISE BUTTON
# =========================

st.write("")

if st.button("🎁 Open Birthday Surprise", use_container_width=True):

    # 🎵 Birthday Music
    try:
        with open("birthday.mp3", "rb") as audio_file:
            audio_bytes = audio_file.read()

        st.audio(
            audio_bytes,
            format="audio/mp3",
            autoplay=True
        )

    except FileNotFoundError:
        st.warning("🎵 Birthday music file was not found.")

    # 🎈 Celebration
    st.balloons()

    st.markdown("""
    <div class="card">

    <div class="message">

    <span class="highlight">
    🎉 A Special Birthday Message 🎉
    </span>

    <div class="divider"></div>

    Wishing you a wonderful birthday
    filled with happiness, success and memorable moments.

    <br><br>

    Thank you for your guidance,
    leadership and continuous support.

    <br><br>

    <strong>
    May the year ahead bring you
    greater achievements and many reasons to celebrate.
    </strong>

    <br><br>

    🌟 <span class="highlight">
    Happy Birthday, Mr. Devbrato Midha!
    </span> 🎂

    </div>

    </div>
    """, unsafe_allow_html=True)


# =========================
# FOOTER
# =========================

st.markdown(
    '<div class="footer">'
    'With Warmest Birthday Wishes ✨<br>'
    '<strong>Er. Neeraj Maurya</strong>'
    '</div>',
    unsafe_allow_html=True
)