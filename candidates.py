#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  candidates.py
#  
#  Copyright 2015 Jackie <Jackie@JACKIE>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


#length 16 height 6 ~2 min
#length 18 height 6 ~10 min

from copy import deepcopy
def create_candidates(length, height):
    grid=[1]*length
    candidates=[]
    while grid[length-1]<=height:
        for left in range(length-1):
			#for clash
            clash=0
            if (grid[left]>1 and grid[left+1]>1):
                clash=1
                #print grid, 'clash'
                for i in range(left+1):
					grid[i]=height
                break
            else:
                for right in range(left+2, length):
                    shortcols=0
                    for middle in range(left+1, right):
                        if grid[middle]<(min(grid[left], grid[right])-1):
                            shortcols+=1
                    if shortcols==(right-(left+1)):
                        clash=1
                        #print grid, 'clash'
                        for i in range(left+1):
					        grid[i]=height
                        break
                if clash==1:
                    break
			#for lapse
            lapse=0
            if left==length-2:
                break
            if grid[left]==grid[left+1]==grid[left+2]:
                lapse=1
                #print grid, 'lapse'
                for i in range(left):
					grid[i]=height
                break
            else:
                for middle in range(left+1, length-1):
                    if grid[middle]==grid[left]:
                        for right in range(middle+1, length):
                            if grid[middle]==grid[right]:
                                shortcols=0
                                for x in range(left+1, right):
                                    if grid[x]<(grid[right]+1):
                                        shortcols+=1
                                if shortcols==(right-(left+1)):
                                    lapse=1
                                    #print grid, 'lapse'
                                    break
                            if lapse==1:
                                break
                    if lapse==1:
                        break
                if lapse==1:
                    break	
        if clash==0 and lapse==0:
			#for too tall
			tootall=0
			for i in range(length):
				if max(grid)>(grid[i]+1):
					tootall+=1
			if tootall==(length-1):
				pass
				#print grid, 'too tall'
				#can you skip with this??
			else:
				#print grid
				candidates.append(deepcopy(grid))
        #print candidates
        grid[0]+=1
        for i in range(length-1):
            if grid[i]>height:
                grid[i]=1
                grid[i+1]+=1
    return candidates


def allcand(length, height):
    grid=[1]*length
    #candidates=[]
    while grid[length-1]<=height:
        #candidates.append(deepcopy(grid))
        print grid
        grid[0]+=1
        for i in range(length-1):
            if grid[i]>height:
                grid[i]=1
                grid[i+1]+=1
    #return candidates

 
if __name__ == '__main__':
    length=input('Enter length: ')
    height=input('Enter height: ')
    #allcand(length, height)
    candlist=create_candidates(length, height)
    print candlist
    
exit()

