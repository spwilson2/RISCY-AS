# RISCY-AS
An elementary assembler for the RISC-V ISA. For simplicity memory is
automatically aligned at 4 byte boundaries.

## Installation 

```
git clone https://github.com/spwilson2/RISCY-AS riscyas
cd riscyas
sudo python3 setup.py install
```

## Development (virtualenv) Install

```
git clone https://github.com/spwilson2/RISCY-AS riscyas
cd riscyas
. develop
```

## Supported RISC-V Instructions
Only a subset of the RV32I ISA will be implemented. The following table lists
supported instructions.

| Format |Args| Instruction |
| :------------- | ---- | ------------------------- |
|LUI  |%rd,$imm| Load Upper Immediate |
|JAL  |%rd,$imm |Jump And Link |
|BEQ  |%rs1,%rs2,$imm| Branch =|
|BNE  |%rs1,%rs2,$imm| Branch != |
|BLT  |%rs1,%rs2,$imm| Branch <|
|BGE  |%rs1,%rs2,$imm| Branch >=|
|BLTU |%rs1,%rs2,$imm|Branch <= Unsigned|
|BGEU |%rs1,%rs2,$imm| Branch >= Unsigned|
|LW   |%rd,%rs1,$imm| Load Word |
|SW   |%rs1,%rs2,$imm|Store Word|
|ADDI |%rd,%rs1,$imm| ADD Immediate|
|XORI |%rd,%rs1,$imm|XOR Immediate |
|ORI  |%rd,%rs1,$imm| OR Immediate|
|ANDI |%rd,%rs1,$imm| AND Immediate|
|ADD  |%rd,%rs1,%rs2| ADD|
|SUB  |%rd,%rs1,%rs2| SUB |
|XOR  |%rd,%rs1,%rs2|XOR|
|OR   |%rd,%rs1,%rs2|OR|
|AND  |%rd,%rs1,%rs2|AND|
|SBREAK||SBREAK|
|NOP||NOP|

## Special Instructions

#### Unimplemented

|Format|Instruction|
|:--|:--|
|;| Comment (Ignore rest of line)|
|dd $imm| Declare Doubleword|

## Instruction Format

Since the assembler is very elementary, input files need to be formatted very
specifically. Instructions should follow the format shown on the supplied green
card or examples.

## Examples

To try assembling an example:

```
riscyas examples/exin.txt examples/exout.bin
```

A quick way to examine the output is to use hexdump: `hexdump -C
examples/exout.bin` (I prefer) `od -t x1 examples/exout.bin`

RISC-AS also supports text output of hex directly!

```
riscyas examples/exin.txt --text
```

#### CHANGELOG

See CHANGELOG.md for brief descriptions of patches. RISCY-AS is currently
under heavy development, so there will likely be many changes to come.
