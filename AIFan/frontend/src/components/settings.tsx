'use client';

import { Card } from '@/components/ui/Card';

export default function Settings() {
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold">Settings</h2>
      <Card className="p-6">
        <div className="space-y-4">
          <div>
            <h3 className="text-lg font-medium">Tweet Generation</h3>
            <p className="text-sm text-gray-400">Configure tweet generation settings</p>
          </div>
          
          <div>
            <h3 className="text-lg font-medium">Voice Settings</h3>
            <p className="text-sm text-gray-400">Configure voice generation parameters</p>
          </div>
          
          <div>
            <h3 className="text-lg font-medium">Theme</h3>
            <p className="text-sm text-gray-400">Customize appearance</p>
          </div>
        </div>
      </Card>
    </div>
  );
}

export { Settings };
