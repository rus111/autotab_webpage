CSS = """
.banner {
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;
    height: 300px;
    text-align: center;
    margin-top: -100px;
    margin-left: -480px;
    margin-right: -480px;
}
.banner h1 {
    padding-top: 120px;
    margin: 0;
    color: white;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    font-size: 56px;
    font-weight: bold;
}
.banner p {
    font-size: 32px;
    color: white;
    opacity: .7;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
}
"""


#######################################################################
# The developers:

developers_html =  """<div class="footer">
<div class="footer-copyright">
    Autotab is brought to you by:
</div>
<img class="avatar-large" alt="avatar-large" src="https://avatars.githubusercontent.com/u/75431042?v=4" />
<img class="avatar-large" alt="avatar-large" src="https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1632725013/gu7bxeeyzt4tvxidmxsu.jpg" />
<img class="avatar-large" alt="avatar-large" src="https://avatars.githubusercontent.com/u/91727688?v=4" />
<img class="avatar-large" alt="avatar-large" src="https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1632729260/u7j3wesevs1hwbtfahem.jpg" />
</div>
"""


developers_css = """
.footer {
  position: fixed;
  bottom:0;
  background: #F4F4F4;
  display: bottom;
  align-items: center;
  justify-content: space-between;
  height: 100px;
  padding: 0px 50px;
  color: rgba(0,0,0,0.3);
}

.avatar {
  width: 40px;
  border-radius: 50%;
}

.avatar-large {
  width: 56px;
  border-radius: 50%;
}

.avatar-bordered {
  width: 40px;
  border-radius: 50%;
  box-shadow: 0 1px 2px rgba(0,0,0,0.2);
  border: white 1px solid;
}

.avatar-square {
  width: 40px;
  border-radius: 0px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.2);
  border: white 1px solid;
}
"""