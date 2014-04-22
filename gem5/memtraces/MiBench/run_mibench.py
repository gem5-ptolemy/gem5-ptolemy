#! /usr/bin/env python

import os
import ntpath

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

maxCycles = 1 * 1000 * 1000
bm_list = []
# automotive
bm_list.append(('automotive/basicmath/basicmath_small',''))
bm_list.append(('automotive/basicmath/basicmath_large',''))
bm_list.append(('automotive/bitcount/bitcnts','75000'))
#bm_list.append(('automotive/qsort/qsort_small','automotive/qsort/qsort_small.dat')) # Abort trap - not enough stack size
#bm_list.append(('automotive/qsort/qsort_large','automotive/qsort/qsort_large.dat')) # Abort trap - not enough stack size
bm_list.append(('automotive/susan/susan',
                'automotive/susan/susan automotive/susan/input_small.pgm automotive/susan/output_small.smoothing.pgm -s'))

# consumer
bm_list.append(('consumer/jpeg/cjpeg',
                '-dct int -progressive -opt -outfile consumer/jpeg/output_small_encode.jpeg consumer/jpeg/input_small.ppm'))
bm_list.append(('consumer/jpeg/djpeg',
                '-dct int -ppm -outfile consumer/jpeg/output_small_decode.ppm consumer/jpeg/input_small.jpg'))
bm_list.append(('consumer/typeset/lout',
                '-I consumer/typeset/include -D consumer/typeset/data -F consumer/typeset/font \
                -C consumer/typeset/maps -H consumer/typeset/hyph small.lout'))
#lame didn't compile no required library 
#mad didn't compile no required library

# network
bm_list.append(('network/dijkstra/dijkstra_small','network/dijkstra/input.dat'))
bm_list.append(('network/dijkstra/dijkstra_large','network/dijkstra/input.dat'))
bm_list.append(('network/patricia/patricia','network/patricia/small.udp'))

# office
# compile error with ghostscript
bm_list.append(('office/stringsearch/search_small',''))
bm_list.append(('office/stringsearch/search_large',''))

# security
bm_list.append(('security/blowfish/bf',
                'e security/blowfish/input_small.asc security/blowfish/output_small.enc 1234567890abcdeffedcba0987654321'))
bm_list.append(('security/sha/sha',
                'e security/sha/input_small.asc'))

# telecomm
bm_list.append(('telecomm/adpcm/rawcaudio','','telecomm/adpcm/small.pcm'))
bm_list.append(('telecomm/adpcm/rawdaudio','','telecomm/adpcm/small.adpcm'))
bm_list.append(('telecomm/CRC32/crc','telecomm/adpcm/small.pcm'))
bm_list.append(('telecomm/FFT/fft','4 4096'))
bm_list.append(('telecomm/gsm/toast',' -fps -c telecomm/gsm/small.au'))


GEM5 = '../../build/ARM/gem5.opt'
GEM5_OPTS = '--outdir='
DEBUG_FLAGS = '--debug-flags=Bus,MemoryAccess --debug-file='
PY_SCRIPT = '../../configs/example/se.py'
PY_OPTS = '--caches --l1d_size=4kB --l1i_size=4kB -m'

for bm in bm_list:
  bm_leaf = path_leaf(bm[0])
  if os.path.isfile(bm_leaf + '.mem'):
    print '\n##### Skipping ' + bm_leaf + ' #####'
    continue
  command = GEM5
  command += ' ' + GEM5_OPTS
  command += bm_leaf + '.out'
  command += ' ' + DEBUG_FLAGS
  command += 'cerr'
  command += ' ' + PY_SCRIPT
  command += ' ' + PY_OPTS
  command += ' ' + str(maxCycles * 500)
  command += ' -c ' + bm[0]
  if len(bm[1]) > 0:
    command += ' -o \"' + bm[1] + "\""
  if len(bm) > 2:
    command += ' < ' + bm[2]
  command += ' 2> ' + bm_leaf + '.mem'
  print '\n##### Trace Generation of ' + bm_leaf + ' #####'
  os.system(command)
  
