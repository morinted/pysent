# pysent

A Python command-line presentation tool.

## Introduction

Presentations just aren't **nerdy** enough, you know? People have their PowerPoints, their Prezis, their Libre/OpenOffice *Impress*. Hah. We scoff at those. No, we need something much nerdier.

While brainstorming this idea, we came up with a solution: what's one place the geek never leaves? The terminal. 

**Question:** Why should you leave the terminal just to make a presentation.

**Answer:** You shouldn't.

## Specifications

We want to make a command-line tool that is easy enough to use for the everyday geek, and still visible when presenting on a projector. For now, it seems like 70 columns is a good width for clear visibility when projected to a screen. It is similar to a 22pt font.

The source file will be specified as an argument, with this simple syntax:

- 5 or more dashes in a row will be considered a new slide.

- The \# sign is used to denounce titles of slides, which will be converted to ASCII-art.

- Every other line of text must be on its own line.

- The specifications will be improved after some usability tests.