from borsh_construct import CStruct, U64
from construct import Bytes, Int8ul, Int32ul, Int64ul, Pass, Switch

PUBLIC_KEY_LAYOUT = Bytes(32)

SPL_ACCOUNT_LAYOUT = CStruct(
    "mint" / PUBLIC_KEY_LAYOUT,
    "owner" / PUBLIC_KEY_LAYOUT,
    "amount" / U64,
    "delegateOption" / Int32ul,
    "delegate" / PUBLIC_KEY_LAYOUT,
    "state" / Int8ul,
    "isNativeOption" / Int32ul,
    "isNative" / U64,
    "delegatedAmount" / U64,
    "closeAuthorityOption" / Int32ul,
    "closeAuthority" / PUBLIC_KEY_LAYOUT
)
SPL_MINT_LAYOUT = CStruct(
  "mintAuthorityOption"/ Int32ul,
  'mintAuthority'/PUBLIC_KEY_LAYOUT,
  'supply'/U64,
  'decimals'/Int8ul,
  'isInitialized'/Int8ul,
  'freezeAuthorityOption'/Int32ul,
  'freezeAuthority'/PUBLIC_KEY_LAYOUT
)