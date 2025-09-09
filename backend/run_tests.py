#!/usr/bin/env python3
"""
Test runner script for the Travel Documentation Assistant API
"""
import os
import subprocess
import sys


def run_tests():
    """Run all tests with pytest"""
    print("🧪 Running tests for Travel Documentation Assistant API...")
    print("=" * 60)
    
    # Change to the backend directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Run pytest with verbose output
    cmd = [
        sys.executable, "-m", "pytest", 
        "test_main.py", 
        "-v", 
        "--tb=short",
        "--color=yes"
    ]
    
    try:
        result = subprocess.run(cmd, check=True)
        print("\n✅ All tests passed!")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Tests failed with exit code {e.returncode}")
        return e.returncode
    except FileNotFoundError:
        print("❌ pytest not found. Please install test dependencies:")
        print("   pip install pytest pytest-asyncio httpx")
        return 1

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)
