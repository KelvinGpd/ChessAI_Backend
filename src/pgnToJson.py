# Convert 5. Bxc8 {[%clk 0:09:28]} 5... Qxc8 {[%clk 0:09:34.2]} --> [..., [ [B, c8, x], [Q, c8, x] ], ...]
# Format : [[2 elements]], [Piece, position, action]
# Eg Nf6 --> [N, f6, null] , e5--> [null, e5, null]

#First letter, if UPPER --> Piece = First letter, else Piece = Null
#Two next letters --> position = Two next letters
#If.. x or - --> Action = x..
#map x --> take...
#(-) --> castle..