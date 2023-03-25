# Graphics Frameworks with Python and OpenGL
Implementing source codes of [Developing Graphics Frameworks with Python and OpenGL](https://www.taylorfrancis.com/books/oa-mono/10.1201/9781003181378/developing-graphics-frameworks-python-opengl-lee-stemkoski-michael-pascale).

Images are from [the author's repositry](https://github.com/stemkoski/Graphics-Framework-Java) for the same concept book for Java.

When I used the book in early 2022, there seemed to be no source codes provided. 
Now, the author or publisher might offer them.

## There are problems
### Adding multi posteffects doesn't work, though it seems that adding only a posteffect works.
The last part of chapter 5 (test-5-12-2.py), test-6-3-combined.py and test-6-4.py of chapter 6 don't work.
It is unclear whether the cause is my mistake or the codes in the book.
I haven't debugged it deeply.

### parametricGeometry.py
When the file is used, a runtime warning appears. It may becaused by the code for **parametricGeometry.py** in the book.

**Runtime warning: invalid value encountered in true_divide**

**normal = normal / numpy.linalg.norm(normal)**

The warning appears when norml = [0., 0., 0.], so probably **Zero Division** happens.

### libpng warning: iCCP: known incorrect sRGB profile
You may clear the warning by opening and resaving png files.

