/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_BACKEND_URL: string
  readonly VITE_RPC_URL: string
  readonly VITE_HELIUS_API_KEY: string
  readonly VITE_BIRDEYE_API_KEY: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}

declare module '@solana/web3.js'
declare module '@solana/wallet-adapter-react' 