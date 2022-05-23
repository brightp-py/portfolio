<!-- shrink header after scrolling -->

<script>
    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
        if (window.pageYOffset > 0) {
            document.getElementById("header_wrap").style.height = "100px";
            document.getElementById("header_wrap").style.backgroundPosition = "center top";
            document.getElementById("content").style.paddingTop = "175px";
        } else {
            document.getElementById("header_wrap").style.height = "100%";
            document.getElementById("header_wrap").style.backgroundPosition = "center center";
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

# Research Assistant

### WordLab

![urs-presentation-2022.jpg](img/urs-presentation-2022.jpg)

I work as a research assistant in Dr. Lisa Levinson's
<a href="https://umwordlab.github.io" target="_blank">WordLab</a>  at UofM. 
Our research focuses on the psycholinguistic properties of human language 
processing. I, in particular, use my experience in computer science to pursue 
the computational side of the topic, using language models to imitate human 
brains.

In simpler terms:

When you read a sentence, you brain has to take some amount of time to process 
each word. Depending on different factors, you make take more or less time to 
process a given word, based on how much effort it requires. Some of this time 
comes from simple factors, like word length and how common it is. Another 
component is **surprisal**, or how surprising it was to find this word in this 
context.

We can simulate surprisal values using computational language models, which 
take a piece of a sentence and provide the probability that a given word 
follows. By taking the negative logarithms of these probabilities, we get 
values that are linearly correlated with reading times (along with other 
related psycholinguistic effects).

Different language models have different capabilities when it comes to 
predicting reading times. Simple models like 
<a href="https://en.wikipedia.org/wiki/N-gram" target="_blank">n-grams</a>, 
for instance, are poor predictors of psycholinguistic effects when n is low 
(bigrams), but improve as n increases.

In my research, I primarily focus on the 
<a href="https://arxiv.org/abs/1602.07776" target="_blank">RNNG</a> model, 
which goes beyond classic language models by building entire syntax trees, 
not just the sentence's words.

![urs-poster.jpg](img/urs-poster.jpg)

---

# Director of Internal Affairs

### FIRST Alumni & Mentor Network at Michigan

When I was in high school, I participated in the 
[FIRST Robotics Competition](https://www.firstinspires.org/robotics/frc), 
where teams of students build robots and use them to compete in tournaments. 
Working in this environment helped me figure out what kind of a team player I 
am, and how to commit to a project with a long term goal.

Plus it was fun.

When I got to college, I was still very excited about the program, and looked 
for other students who had participated. At some point, I happened across the 
FIRST logo drawn in chalk on the ground, with a time and place for an 
introductory meeting for a club: the FIRST Alumni & Mentor Network at 
Michigan (FAMNM). The group's goal was to get college students involved in 
mentoring high school teams and volunteering at FIRST events.

I signed up and gave it my all. I ended up giving a presentation on scouting 
other teams' stats just two months after joining the group, and I attended 
everything I could.

<table width="100%" table-layout="fixed">
<tr>
<td>
    <img src="img\famnm-smile.jpg" width="300"/>
</td>
<td class="center_element">
    <p>
        Baby me, when I first signed up for FAMNM.
    </p>
    <p>
        September, 2019
    </p>
</td>
</tr>
</table>

After a year of being an active member, and just after the onset of the 
pandemic, I was voted in as the group's Director of Internal Affairs. This 
gave me about the same authority as the Vice President, and was a really big 
responsibility when there was, y'know, a pandemic going on.

For two years, I worked hard to hold the organization together in a new 
remote format. This meant getting a lot of practice keeping Zoom meetings 
engaging, designing a new format for each term's elections, and scheduling 
times for members to just meet up and play games to stay involved.

More than anything, my time as the Director of Internal Affairs was spent 
keeping the club stable through an extremely turbulent time. As in-person 
events we relied on were canceled, outreach opportunities were lost, and 
participation waned, it became our goal to just keep FAMNM's torch burning.

And we succeeded.

Now, as we get back into the swing of things, it's time to add more fuel to 
that fire. For my final term participating in FAMNM, I've taken on the 
position of Director of Marketing, meaning I'll be heading all of our 
outreach and recruitment efforts.

To get people involved in FIRST Robotics again, we'll need to give students a 
chance to meet up with their fellow FIRST alumni to chat and build 
connections. We'll need clear instructions on how to get involved with teams 
and volunteering. And we'll need exciting ways to make our organization 
visible to the whole student body.

In the end, my goal is to leave this amazing club as I found it, but refreshed 
and stronger than it ever was before.

---

# Pythonista

### Numpad Programming Language

<textarea id="phrase" rows="15" cols="85" class="code_write"></textarea>

<div class="center">
    <button id="convert" pys-onClick="convert">Convert</button>
</div>

<code id="display" box-shadow="transparent">Add Numpad code to the box above and hit "Convert".
</code>

Copy the full code, including necessary helper functions, here:

<textarea readonly id="save" rows="5" cols="85" onfocus="this.select()">
Add Numpad code to the box above and hit "Convert".
</textarea>

---

# COVID-19 Volunteer Coordinator

### Helpful Engineering

---

# Data Scientist (and World Champion)

### FIRST Team 3707

---

# Proof I know how to use things

I do a lot of stuff. And I often have to use new things to do that stuff.

Here are some examples.

## Adobe Premiere Pro

<iframe width="640" height="426.6" src="https://www.youtube.com/embed/7Vv11KY3yNA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## HTML and CSS

\*Gestures broadly.\*

## Latex

See <a href="https://drive.google.com/file/d/16EEwpLGouQf3BKBLO61QS2T7zz3hhcAe/view?usp=sharing" target="_blank">
my notes from Differential Equations</a>

<!-- main pyscript code -->

<py-script>
from numpad_parse import convert_to_python

in_ = Element("phrase")
out = Element("display")
save = Element("save")

def convert(*args, **kwargs):
    to_save, to_show = convert_to_python(in_.value)
    out.write(to_show)
    save.write(to_save)
</py-script>