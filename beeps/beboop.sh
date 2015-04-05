#!/bin/bash

#beeper

play -n synth 0.2 sine 1000
play -n synth 0.5 sine 800-2000
play -n synth 0.1 saw 1000-100

for i in E2, A2, D3, G3, B3, E4; do
     play −n synth 1 pluck $i
done

play -n synth 1 pluck E2
play -n synth 1 pluck A2
play -n synth 1 pluck D3
