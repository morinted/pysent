# pysent

A Python command-line presentation tool.

## Introduction

Presentations just aren't **nerdy** enough, you know? People have their PowerPoints, their Prezis, their Libre/OpenOffice *Impress*. Hah. We scoff at those. No, we need something much nerdier.

While brainstorming this idea, we came up with a solution: what's one place the geek never leaves? The terminal. 

**Question:** Why should you leave the terminal just to make a presentation?

**Answer:** You shouldn't.

## Instructions

We want to make a command-line tool that is easy enough to use for the everyday console-geek, and still viewable when presenting on a projector. For now, it seems like 70 columns and 22 rows are a good width and height for clear visibility when projected to a screen. It is similar to a 22pt font. The script uses variables row and col that can be changed according to your needs.

The source file will be specified as an argument, with this simple syntax:

- 5 or more dashes in a row will be considered a new slide.

- The \# sign is used to denounce titles of slides, which will be converted to ASCII-art. Only one title per slide.

- Only bullet points without tabs will be taken. Bullets can be "-" or a digit followed by a period (e.g: 2.)

Current usage: {python pysent.py -i <inputfile>}

Every point will be displayed after hitting Enter. When the last point of the slide is displayed, a slide indicator will show. When the last slide is done, a thicker line is displayed and then a black screen will show, similar to the opening screen.

To go back a slide, after a point is displayed, the user must type {p} and hit Enter.