#source_github_Wojtasny
import random
import time
current_tilt = 0
max_correction = 10
correction = 0

def get_new_angle(current_tilt):
	new_angle = random.gauss(0, 30)
	current_tilt = current_tilt + new_angle
	return current_tilt

def get_correction(current_tilt):
	if abs(current_tilt) > max_correction:
		correction = max_correction
		if current_tilt > 0:
			current_tilt = current_tilt - max_correction
		else:
			current_tilt = current_tilt + max_correction
	else:
		correction = 0 - current_tilt
		current_tilt = 0
	return correction

if __name__ == "__main__":
	while True:
		current_tilt = get_new_angle(current_tilt)
		print "Current tilt = " + str(current_tilt)
		correction = get_correction(current_tilt)
		print "Tilt correction = " + str(correction)	
		time.sleep(0.5)


