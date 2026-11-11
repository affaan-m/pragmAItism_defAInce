'use client';

import { FC } from 'react';

interface SidebarProps {
  currentPage: string;
  setCurrentPage: (page: string) => void;
}

export const Sidebar: FC<SidebarProps> = ({ currentPage, setCurrentPage }) => {
  const menuItems = [
    { id: 'tweet-generator', label: 'Tweet Generator' },
    { id: 'token-stats', label: 'Token Stats' },
    { id: 'analytics', label: 'Analytics' },
    { id: 'settings', label: 'Settings' }
  ];

  return (
    <aside className="w-64 bg-gray-900 p-6">
      <h1 className="text-xl font-bold mb-8">AI Fan Dashboard</h1>
      <nav>
        <ul className="space-y-4">
          {menuItems.map((item) => (
            <li key={item.id}>
              <button
                onClick={() => setCurrentPage(item.id)}
                className={`w-full text-left px-4 py-2 rounded ${
                  currentPage === item.id 
                    ? 'bg-blue-600' 
                    : 'hover:bg-gray-800'
                }`}
              >
                {item.label}
              </button>
            </li>
          ))}
        </ul>
      </nav>
    </aside>
  );
}; 