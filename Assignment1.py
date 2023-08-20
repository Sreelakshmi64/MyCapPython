'''#Code 1

# Calculatig area of a circle
import numpy    #imoprting the numpy library in python to call 'numpy.pi' function
r=float(input("Enter the radius of the circle"))    #getting the radius of the circle form the user
units=input("Enter the unit of the radius(eg: m, cm, mm, ft, etc.,)")   #getting the unit of measurement from the user
Area=(numpy.pi)*(r**2)    #calculating the area of the circle with the input radius
print("The area of the circle with input radius,'r='",r,units,"is",Area,units+"^2")    #printing the area'''

#Code 2

# Printing the extension of the input filename
dic={".txt": "Text File",
    ".doc": "Microsoft Word Document",
    ".docx": "Microsoft Word Open XML Document",
    ".pdf": "Portable Document Format",
    ".csv": "Comma-Separated Values",
    ".xlsx": "Microsoft Excel Open XML Spreadsheet",
    ".ppt": "Microsoft PowerPoint Presentation",
    ".pptx": "Microsoft PowerPoint Open XML Presentation",
    ".jpg": "JPEG Image",
    ".jpeg": "JPEG Image",
    ".png": "PNG Image",
    ".gif": "GIF Image",
    ".bmp": "Bitmap Image",
    ".mp3": "MP3 Audio",
    ".wav": "Waveform Audio",
    ".mp4": "MP4 Video",
    ".avi": "Audio Video Interleave",
    ".mkv": "Matroska Video",
    ".zip": "Zip Archive",
    ".rar": "RAR Archive",
    ".tar": "Tape Archive",
    ".gz": "Gzip Compressed Archive",
    ".exe": "Executable File",
    ".dll": "Dynamic Link Library",
    ".html": "Hypertext Markup Language",
    ".css": "Cascading Style Sheet",
    ".js": "JavaScript",
    ".py": "Python Script",
    ".cpp": "C++ Source Code",
    ".java": "Java Source Code",
    ".py": "Python"
}    # feeding the file extensions into python as a dictionary   
file_name=input("Enter the file name")    #getting the file name from the user
l=file_name.split(".",)    #seperating the file name and the file extension
extension="."+l[-1]    #extracting the file extension alone
if extension in dic:
    file_type=dic[extension]    #collecting the file type from the dictionary
    print("The file is a",file_type)    #printing the file type
else:
    print("Extension Not Found")