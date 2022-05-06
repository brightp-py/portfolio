<!-- shrink header after scrolling -->

<script>
    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
        if (window.pageYOffset > 0) {
            document.getElementById("header_wrap").style.height = "100px";
            document.getElementById("content").style.paddingTop = "175px";
        } else {
            document.getElementById("header_wrap").style.height = "100%";
            document.getElementById("content").style.paddingTop = "150%";
        }
    }
</script>

<!-- links to other sites -->

<div id="content" markdown="1">
<table width="100%" table-layout="fixed">
<tr>
<td class="center_element">
    <a href="https://github.com/brightp-py" target="_blank">
        <img src="img\logos\github.png" width="100"/>
    </a>
</td>
<td class="center_element">
    <a href="https://www.youtube.com/channel/UC6txpOCWxeZI_KPf4LClS6A" target="_blank">
        <img src="img\logos\youtube.svg" width="100"/>
    </a>
</td>
<td class="center_element">
    <a href="https://www.linkedin.com/in/brighton-p-9569a7194/" target="_blank">
        <img src="img\logos\linkedin.svg" width="100"/>
    </a>
</td>
<td class="center_element">
    <a href="https://leetcode.com/brightp/" target="_blank">
        <img src="img\logos\leetcode.png" width="100"/>
    </a>
</td>
</tr>
</table>

---

![urs-presentation-2022.jpg](img/urs-presentation-2022.jpg)

![urs-poster.jpg](img/urs-poster.jpg)

---

<table width="100%">
<tr>
<td width="50%" class="code_box">
    <textarea id="phrase" rows="15" cols="40" class="code_write"></textarea>
    <!-- <py-inputbox id="phrase"></py-inputbox> -->
</td>
<td class="code_box">
    <code id="display" box-shadow="transparent"></code>
</td>
</tr>
</table>

<div><button id="convert" pys-onClick="convert">
Convert
</button></div>
</div>

<!-- main pyscript code -->

<py-script>
in_ = Element("phrase")
out = Element("display")

def convert(*args, **kwargs):
    out.write(in_.value)
</py-script>