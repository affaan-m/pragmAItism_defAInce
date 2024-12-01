import { Routes, Route } from 'react-router-dom'
import { Navigation } from '@/components/navigation'
import { Welcome } from '@/components/welcome'
import { Providers } from './providers'

zsh:1: command not found: wq
import TalkToMe from './routes/talk-to-me/page'
import IWantToFeel from './routes/i-want-to-feel/page'
import AmIAFake from './routes/amiafake/page'
import NeuralLink from './routes/neural-link/page'

export default function App() {
  return (
    <Providers>
      <div className="min-h-screen bg-background text-foreground">
        <Navigation />
        <Welcome />
        <main className="container mx-auto px-4 py-8">
          <Routes>
            <Route path="/" element={<Welcome />} />
            <Route path="/talk-to-me" element={<TalkToMe />} />
            <Route path="/i-want-to-feel" element={<IWantToFeel />} />
            <Route path="/am-i-a-fake" element={<AmIAFake />} />
            <Route path="/neural-link" element={<NeuralLink />} />
          </Routes>
        </main>
      </div>
    </Providers>
  )
}

