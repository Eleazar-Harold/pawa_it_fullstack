#!/usr/bin/env node
/**
 * Test runner script for the Travel Documentation Assistant Frontend
 */
const { spawn } = require('child_process');
const path = require('path');

function runTests() {
  console.log('🧪 Running tests for Travel Documentation Assistant Frontend...');
  console.log('=' * 60);
  
  const testCommand = process.argv[2] || 'test';
  const args = process.argv.slice(3);
  
  let command, commandArgs;
  
  switch (testCommand) {
    case 'watch':
      command = 'npm';
      commandArgs = ['run', 'test:watch'];
      break;
    case 'coverage':
      command = 'npm';
      commandArgs = ['run', 'test:coverage'];
      break;
    case 'ci':
      command = 'npm';
      commandArgs = ['run', 'test', '--', '--ci', '--coverage', '--watchAll=false'];
      break;
    default:
      command = 'npm';
      commandArgs = ['run', 'test'];
  }
  
  // Add any additional args
  commandArgs.push(...args);
  
  const child = spawn(command, commandArgs, {
    stdio: 'inherit',
    shell: true,
    cwd: path.resolve(__dirname)
  });
  
  child.on('close', (code) => {
    if (code === 0) {
      console.log('\n✅ All tests passed!');
    } else {
      console.log(`\n❌ Tests failed with exit code ${code}`);
    }
    process.exit(code);
  });
  
  child.on('error', (error) => {
    console.error('❌ Failed to start test process:', error);
    process.exit(1);
  });
}

if (require.main === module) {
  runTests();
}

module.exports = { runTests };
