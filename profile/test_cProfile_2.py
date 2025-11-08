# test cProfile and tuna
# run cProfile: python3 -m cProfile -o OpenGLContext.profile  test.py with test.py is file execute, -o is output file, OpenGLContext.profile is output file, can be .out, .profile, .prof
# run tuna: tuna OpenGLContext.profile
import cProfile
command = """[i for i in range(10)]"""
cProfile.runctx( command, globals(), locals(), filename="OpenGLContext.profile" )