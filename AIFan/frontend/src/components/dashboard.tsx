'use client'

import { TweetGenerator } from './tweet-generator'
import { TokenStats } from './token-stats'
import { Analytics } from './analytics'
import { Settings } from './settings'

interface DashboardProps {
  currentPage: string
}

export const Dashboard: React.FC<DashboardProps> = ({ currentPage }) => {
  const renderContent = () => {
    switch (currentPage) {
      case 'tweet-generator':
        return <TweetGenerator />
      case 'token-stats':
        return <TokenStats />
      case 'analytics':
        return <Analytics />
      case 'settings':
        return <Settings />
      default:
        return <TweetGenerator />
    }
  }

  return (
    <div className="max-w-4xl mx-auto">
      {renderContent()}
    </div>
  )
} 