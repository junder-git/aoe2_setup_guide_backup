﻿$XButton2::
    Send, {F11}
    Sleep, ms
    Send, {F11}
    Sleep, ms
    Send, {XButton2}
return

$XButton1::
    Send, {F11}
    Sleep, ms
    Send, {XButton1}
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