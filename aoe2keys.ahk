;1- In aoe2change the cancel the build menu with defaut "b" key to F11, 
;2- build economy default "q" to F12. 
;3- set any build key to any of the alphabet in aoe2 villager build section 

$XButton2:: ; Garrison and Set gather point and Select all town centers
    Send, {F11}
    Sleep, ms
    Send, {F11}
    Sleep, ms
    Send, {XButton2}
return


BuildBuilding(key, ms:=30)
{
    Send, {F11}
    Sleep, ms
    Send, {F12}
    Sleep, ms
    Send, %key%
    return
}

$a::BuildBuilding("a")
$b::BuildBuilding("b")
$c::BuildBuilding("c")
$d::BuildBuilding("d")
$e::BuildBuilding("e")
$f::BuildBuilding("f")
$g::BuildBuilding("g")
$h::BuildBuilding("h")
$i::BuildBuilding("i")
$j::BuildBuilding("j")
$k::BuildBuilding("k")
$l::BuildBuilding("l")
$m::BuildBuilding("m")
$n::BuildBuilding("n")
$o::BuildBuilding("o")
$p::BuildBuilding("p")
$q::BuildBuilding("q")
$r::BuildBuilding("r")
$s::BuildBuilding("s")
$t::BuildBuilding("t")
$u::BuildBuilding("u")
$v::BuildBuilding("v")
$w::BuildBuilding("w")
$x::BuildBuilding("x")
$y::BuildBuilding("y")
$z::BuildBuilding("z")


;up and down arrows --> Zoom
;mouse wheel up/down --> rotate gate
;F11 --> villager build