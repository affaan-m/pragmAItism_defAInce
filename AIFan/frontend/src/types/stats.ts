export interface TokenStats {
  price: number;
  change_24h: number;
  volume: number;
  history: Array<{
    timestamp: string;
    value: number;
  }>;
} 