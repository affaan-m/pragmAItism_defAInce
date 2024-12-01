import { Connection, PublicKey, LAMPORTS_PER_SOL } from '@solana/web3.js';

const RPC_URL = import.meta.env.VITE_RPC_URL || 'https://api.mainnet-beta.solana.com';
const connection = new Connection(RPC_URL);

interface TokenBalance {
  balance: number;
  uiBalance: number;
}

export const solanaService = {
  getBalance: async (address: string | typeof PublicKey): Promise<TokenBalance> => {
    const pubKey = typeof address === 'string' ? new PublicKey(address) : address;
    const balance = await connection.getBalance(pubKey);
    return {
      balance,
      uiBalance: balance / LAMPORTS_PER_SOL
    };
  }
}; 