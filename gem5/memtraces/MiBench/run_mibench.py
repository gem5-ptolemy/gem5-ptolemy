#! /usr/bin/env python

import os
import ntpath

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

maxCycles = 1 * 1000 * 1000
bm_list = []
# automotive
bm_list.append(('basicmath_small','automotive/basicmath/basicmath_small',''))
bm_list.append(('basicmath_large','automotive/basicmath/basicmath_large',''))
bm_list.append(('bitcount_small','automotive/bitcount/bitcnts','75000'))
bm_list.append(('bitcount_large','automotive/bitcount/bitcnts','1125000'))
#bm_list.append(('automotive/qsort/qsort_small','automotive/qsort/qsort_small.dat')) # Abort trap - not enough stack size
#bm_list.append(('automotive/qsort/qsort_large','automotive/qsort/qsort_large.dat')) # Abort trap - not enough stack size
bm_list.append(('susan_small','automotive/susan/susan',
                'automotive/susan/input_small.pgm automotive/susan/output_small.smoothing.pgm -s'))
bm_list.append(('susan_large','automotive/susan/susan',
                'automotive/susan/input_large.pgm automotive/susan/output_large.smoothing.pgm -s'))

# consumer
bm_list.append(('cjpeg_small','consumer/jpeg/cjpeg',
                '-dct int -progressive -opt -outfile consumer/jpeg/output_small_encode.jpeg consumer/jpeg/input_small.ppm'))
bm_list.append(('cjpeg_large','consumer/jpeg/cjpeg',
                '-dct int -progressive -opt -outfile consumer/jpeg/output_large_encode.jpeg consumer/jpeg/input_large.ppm'))
bm_list.append(('djpeg_small','consumer/jpeg/djpeg',
                '-dct int -ppm -outfile consumer/jpeg/output_small_decode.ppm consumer/jpeg/input_small.jpg'))
bm_list.append(('djpeg_large','consumer/jpeg/djpeg',
                '-dct int -ppm -outfile consumer/jpeg/output_large_decode.ppm consumer/jpeg/input_large.jpg'))
bm_list.append(('typeset_small','consumer/typeset/lout',
                '-I consumer/typeset/include -D consumer/typeset/data -F consumer/typeset/font \
                -C consumer/typeset/maps -H consumer/typeset/hyph consumer/typeset/small.lout'))
bm_list.append(('typeset_large','consumer/typeset/lout',
                '-I consumer/typeset/include -D consumer/typeset/data -F consumer/typeset/font \
                -C consumer/typeset/maps -H consumer/typeset/hyph consumer/typeset/large.lout'))
#lame didn't compile no required library 
#mad didn't compile no required library

# network
bm_list.append(('dijkstra_small','network/dijkstra/dijkstra_small','network/dijkstra/input.dat'))
bm_list.append(('dijkstra_large','network/dijkstra/dijkstra_large','network/dijkstra/input.dat'))
bm_list.append(('patricia_small','network/patricia/patricia','network/patricia/small.udp'))
bm_list.append(('patricia_large','network/patricia/patricia','network/patricia/large.udp'))

# office
# compile error with ghostscript
bm_list.append(('search_small','office/stringsearch/search_small',''))
bm_list.append(('search_large','office/stringsearch/search_large',''))

# security
bm_list.append(('blowfish_small','security/blowfish/bf',
                'e security/blowfish/input_small.asc security/blowfish/output_small.enc 1234567890abcdeffedcba0987654321'))
bm_list.append(('blowfish_large','security/blowfish/bf',
                'e security/blowfish/input_large.asc security/blowfish/output_large.enc 1234567890abcdeffedcba0987654321'))
bm_list.append(('rijndael_small','security/rijndael/rijndael',
                'security/rijndael/input_small.asc security/rijndael/output_small.enc\
                 e 1234567890abcdeffedcba09876543211234567890abcdeffedcba0987654321'))
bm_list.append(('rijndael_large','security/rijndael/rijndael',
                'security/rijndael/input_large.asc security/rijndael/output_large.enc\
                 e 1234567890abcdeffedcba09876543211234567890abcdeffedcba0987654321'))
bm_list.append(('sha_small','security/sha/sha',
                'e security/sha/input_small.asc'))
bm_list.append(('sha_large','security/sha/sha',
                'e security/sha/input_large.asc'))

# telecomm
bm_list.append(('adpcm_rawcaudio_small','telecomm/adpcm/rawcaudio','','telecomm/adpcm/small.pcm'))
bm_list.append(('adpcm_rawdaudio_small','telecomm/adpcm/rawdaudio','','telecomm/adpcm/small.adpcm'))
bm_list.append(('adpcm_rawcaudio_large','telecomm/adpcm/rawcaudio','','telecomm/adpcm/large.pcm'))
bm_list.append(('adpcm_rawdaudio_large','telecomm/adpcm/rawdaudio','','telecomm/adpcm/large.adpcm'))
bm_list.append(('CRC_small','telecomm/CRC32/crc','telecomm/adpcm/small.pcm'))
bm_list.append(('CRC_large','telecomm/CRC32/crc','telecomm/adpcm/large.pcm'))
bm_list.append(('FFT_small','telecomm/FFT/fft','4 4096'))
bm_list.append(('FFT_large','telecomm/FFT/fft','8 32768'))
bm_list.append(('gsm_small','telecomm/gsm/toast',' -fps -c telecomm/gsm/small.au'))
bm_list.append(('gsm_large','telecomm/gsm/toast',' -fps -c telecomm/gsm/large.au'))


GEM5 = '../../build/ARM/gem5.opt'
GEM5_OPTS = '--outdir='
DEBUG_FLAGS = '--debug-flags=Bus,MemoryAccess --debug-file='
PY_SCRIPT = '../../configs/example/se.py'
PY_OPTS = '--caches --l1d_size=4kB --l1i_size=4kB -m'

for bm in bm_list:
  bm_name = bm[0]
  bm_path = bm[1]
  bm_args = bm[2]
  bm_redirect = ''
  if len(bm) > 3:
    bm_redirect = bm[3]
  #bm_leaf = path_leaf(bm_path)
  if os.path.isfile(bm_name + '.mem'):
    print '\n##### Skipping ' + bm_name + ' #####'
    continue
  command = GEM5
  command += ' ' + GEM5_OPTS
  command += bm_name + '.out'
  command += ' ' + DEBUG_FLAGS
  command += 'cerr'
  command += ' ' + PY_SCRIPT
  command += ' ' + PY_OPTS
  command += ' ' + str(maxCycles * 500)
  command += ' -c ' + bm_path
  if len(bm_args) > 0:
    command += ' -o \"' + bm_args + "\""
  if len(bm_redirect) > 0:
    command += ' < ' + bm_redirect
  command += ' 2> ' + bm_name + '.mem'
  print '\n##### Trace Generation of ' + bm_name + ' #####'
  os.system(command)
  
