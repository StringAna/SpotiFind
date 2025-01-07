import React from 'react';
import { Search, Share2, Heart } from 'lucide-react';
import { FloatingIcons } from './components/FloatingIcons';
import { SpotifyButton } from './components/SpotifyButton';
import { FeatureCard } from './components/FeatureCard';
import { Equalizer } from './components/Equalizer';

function App() {
  return (
    <div className="min-h-screen bg-background text-white relative overflow-hidden">
      <FloatingIcons />
      
      <div className="container mx-auto px-4 py-16 relative z-10">
        <div className="flex flex-col items-center justify-center min-h-[80vh] text-center">
          <div className="mb-8 flex items-center gap-2">
            <Equalizer />
            <h1 className="text-6xl font-bold bg-gradient-to-r from-primary to-secondary text-transparent bg-clip-text">
              Spotifind
            </h1>
            <Equalizer />
          </div>
          
          <p className="text-xl text-gray-400 mb-12 max-w-2xl mx-auto animate-fade-in">
            Discover your next favorite song and share the magic of music with people who get it.
          </p>

          <SpotifyButton />
          <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto mt-16">
          <FeatureCard
            icon={Search}
            title="Discover"
            description="Find new music based on your unique taste and listening patterns"
          />
          <FeatureCard
            icon={Share2}
            title="Share"
            description="Create and share personalized playlists with friends and followers"
          />
          <FeatureCard
            icon={Heart}
            title="Connect"
            description="Match with people who share your musical wavelength"
          />
        </div>
        </div>

        
      </div>
    </div>
  );
}

export default App;