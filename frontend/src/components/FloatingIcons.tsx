import React from 'react';
import { Music, Headphones, Disc, Heart, Radio } from 'lucide-react';

const icons = [Music, Headphones, Disc, Heart, Radio];

export function FloatingIcons() {
  return (
    <div className="fixed inset-0 pointer-events-none overflow-hidden">
      {[...Array(15)].map((_, i) => {
        const Icon = icons[i % icons.length];
        const size = 20 + Math.random() * 30;
        const left = Math.random() * 100;
        const animationDelay = Math.random() * 30;
        const duration = 20 + Math.random() * 10;

        return (
          <div
            key={i}
            className="absolute text-white/10 animate-float"
            style={{
              left: `${left}%`,
              top: '-50px',
              width: `${size}px`,
              height: `${size}px`,
              animationDelay: `${animationDelay}s`,
              animationDuration: `${duration}s`,
            }}
          >
            <Icon size={size} />
          </div>
        );
      })}
    </div>
  );
}