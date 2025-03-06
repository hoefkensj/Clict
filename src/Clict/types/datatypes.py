from dataclasses import dataclass,field
from enum import Enum
@dataclass()
class SymbolSet(Enum):
	TLC : str=field(default='')
	TRC : str=field(default='')
	VLT : str=field(default='')
	VRT : str=field(default='')
	BLC : str=field(default='')
	BRC : str=field(default='')
	HTT : str=field(default='')
	HBT : str=field(default='')
	HFL : str=field(default='')
	VFL : str=field(default='')

BOXDRAW_DOUBLE_tree=SymbolSet()
tree.BLC = '┗'
tree.HFL = '━'
tree.VLT = '┣'
tree.HTT = '┳'
tree.NODE ='╼'
tree.VFL = '┃'



