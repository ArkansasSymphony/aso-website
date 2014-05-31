# my enumerators
import datetime

######################################
## enum misc functions
######################################

## used in retrieving the current year for enums
def current_year():
	return int(datetime.datetime.now().year)

###################################### 
## ENUMS FOR INSTRUMENTS
######################################
INST_TYPE = (
		('String','String'),
		('Woodwind','Woodwind'),
		('Brass','Brass'),
		('Keyboards and Harp','Keyboards and Harp'),
		('Percussion','Percussion'),
		)

INSTRUMENTS = (
	('Violin','Violin'),
	('Viola','Viola'),
	('Cello','Cello'),
	('Bass','Bass'),
	('Flute','Flute'),
	('Piccolo','Piccolo'),
	('Oboe','Oboe'),
	('Clarinet','Clarinet'),
	('English Horn','English Horn'),
	('Clarinet','Clarinet'),
	('Bass Clarinet','Bass Clarinet'),
	('Bassoon','Bassoon'),
	('Contrabassoon','Contrabassoon'),
	#('Saxophone','Saxophone'),
	('Trumpet','Trumpet'),
	('French Horn','French Horn'),
	('Trombone','Trombone'),
	('Tuba','Tuba'),
	#('Celesta','Celesta'),
	('Piano/Keyboard','Piano/Keyboard'),
	#('Harpsichord','Harpsichord'),
	#('Organ','Organ'),
	#('Synthesizer','Synthesizer'),
	('Harp','Harp'),
	('Timpani','Timpani'),
	#('Snare Drum','Snare Drum'),
	('Percussion','Percussion'),
	#('Bass Drum','Bass Drum'),
	#('Cymbals','Cymbals'),
	#('Tambourine','Tambourine'),
	#('Triangle','Triangle'),
	#('Xylophone','Xylophone'),
	#('Glockenspiel','Glockenspiel'),
	#('Chimes','Chimes'),
	#('Marimba','Marimba'),
	#('Vibraphone','Vibraphone'),
	)

#####################################
## GLOBAL ENUMS (can be used for other pick lists)
#####################################

PRIMARY_NUMBER = (
	('Cell','Cell'),
	('Home','Home'),
	('Other', 'Other'),
	)

PREFERRED_COM_METHOD = (
	('Email','Email'),
	('Phone','Phone'),
	)

YES_NO = (
	('Y','Yes'),
	('N','No'),
	)

STATUS = (
	('A', 'Active'),
	('I','Inactive'),
	('D', 'Dropped'),
	)

ORCHESTRA_TYPE = (
	('Preparatory','Preparatory'),
	('Prelude','Prelude'),
	('Academy','Academy'),
	('Youth','Youth'),
	)

PAID_STATUS = (
	('Y','Yes'),
	('N','No'),
	('S','Scholarship'),
	('O','Other'),
	('P','Paid'),
	)

GRAD_YEAR = (
	('2014', '2014'),
	('2015', '2015'),
	('2016', '2016'),
	('2017', '2017'),
	('2018', '2018'),
	('2019', '2019'),
	('2020', '2020'),
	('2021', '2021'),
	('2022', '2022'),
	('2023', '2023'),
	)

GRADE_LEVEL = tuple([(str(grade),str(grade)) for grade in range(0,13)])

YEARS = tuple([year for year in range(1995,2055)])

ENUM_YEARS = (
	(current_year(),current_year()),
	)

AGE = tuple([(age,age) for age in range(1,19)])
