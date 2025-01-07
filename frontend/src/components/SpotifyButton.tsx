import React from 'react';
import { Music2 } from 'lucide-react';

export function SpotifyButton() {
  return (
    <button className="group relative px-8 py-4 bg-spotify hover:bg-spotify/90 text-white rounded-full font-semibold text-lg transition-all duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-spotify/50 focus:ring-offset-2 focus:ring-offset-background">
      <div className="absolute inset-0 rounded-full bg-gradient-to-r from-spotify to-spotify/80 animate-pulse opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
      <span className="relative flex items-center gap-2">
        <Music2 className="w-6 h-6" />
        Connect with Spotify
      </span>
    </button>
  );
}