import os, glob, time

#base_dir = '/sys/devices/w1_bus_master/'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'
device_file = '/sys/devices/w1_bus_master1/28-00000698ec20/w1_slave'
device_file2= '/sys/devices/w1_bus_master1/28-000006908a86/w1_slave'

# Raw temperature function
def read_temp_raw(df):
 f = open(df, 'r')
 lines = f.readlines()
 f.close()
 #print lines
 return lines

# Temperature conversion function
def read_temp(df):
 lines = read_temp_raw(df)
 while lines[0].strip()[-5:] != 'YES\n':
  time.sleep(0.2)
  lines = read_temp_raw(df)
  # Parse the lines to find the temperature 
  equals_pos = lines[1].find('t=')
  if equals_pos != -1:
   # Store the temperature, which is in the 2nd field
   temp_string = lines[1][equals_pos+2:]
   # Format the celsius temperature
   temp_c = float(temp_string) / 1000.0
   # Return the temperature values
   return temp_c

def main():
 #while True:
  # Take a temperature reading
  temp_c = []
  temp_c.append(read_temp(device_file))
  temp_c.append(read_temp(device_file2))
  return temp_c
  # Print temperature in Celsius to screen
  #print 'Temperature = {0} C'.format(temp_c)
  #time.sleep(1)

if __name__ == '__main__':
 main()
