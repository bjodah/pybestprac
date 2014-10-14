#include <vector>
#include <stdexcept>
#include "euclid.h"

using std::vector;

vector<double>
euclid::euclidean_norm(vector<vector<int> > vecs){
  vector<double> r; // result
  r.reserve(vecs.size());
  for (auto v : vecs){
    if (v.size() == 0)
      throw std::length_error("Cannot take norm of zero length vector.");
    r.push_back(euclid::enorm_enorm2_(v.size(), &v[0]));
  }
  return r;
}
